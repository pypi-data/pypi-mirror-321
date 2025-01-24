#! /usr/bin/env python


import sys
import re
import tempfile
import subprocess
import logging
import os
import importlib
import inspect
import platform

__version__ = '0.1.8'
__version_info__ = (0,1,8)

class _LoggerObject(object):
    def __init__(self,logname='disttools'):
        self.__logger = logging.getLogger(logname)
        if len(self.__logger.handlers) == 0:
            loglvl = logging.WARN
            lvlname = '%s_LOGLEVEL'%(logname.upper())
            if lvlname in os.environ.keys():
                v = os.environ[lvlname]
                vint = 0
                try:
                    vint = int(v)
                except:
                    vint = 0
                if vint >= 4:
                    loglvl = logging.DEBUG
                elif vint >= 3:
                    loglvl = logging.INFO
            handler = logging.StreamHandler()
            fmt = "%(levelname)-8s %(message)s"
            logfmtname = '%s_LOGFMT'%(logname.upper())
            if logfmtname in os.environ.keys():
                v = os.environ[logfmtname]
                if v is not None and len(v) > 0:
                    fmt = v
            formatter = logging.Formatter(fmt)
            handler.setFormatter(formatter)
            self.__logger.addHandler(handler)
            self.__logger.setLevel(loglvl)

    def format_string(self,arr):
        s = ''
        if isinstance(arr,list):
            i = 0
            for c in arr:
                s += '[%d]%s\n'%(i,c)
                i += 1
        elif isinstance(arr,dict):
            for c in arr.keys():
                s += '%s=%s\n'%(c,arr[c])
        else:
            s += '%s'%(arr)
        return s

    def format_call_msg(self,msg,callstack):
        inmsg = ''  
        if callstack is not None:
            try:
                frame = sys._getframe(callstack)
                inmsg += '[%-10s:%-20s:%-5s] '%(frame.f_code.co_filename,frame.f_code.co_name,frame.f_lineno)
            except:
                inmsg = ''
        inmsg += msg
        return inmsg

    def info(self,msg,callstack=1):
        inmsg = msg
        if callstack is not None:
            inmsg = self.format_call_msg(msg,(callstack + 1))
        return self.__logger.info('%s'%(inmsg))

    def error(self,msg,callstack=1):
        inmsg = msg
        if callstack is not None:
            inmsg = self.format_call_msg(msg,(callstack + 1))
        return self.__logger.error('%s'%(inmsg))

    def warn(self,msg,callstack=1):
        inmsg = msg
        if callstack is not None:
            inmsg = self.format_call_msg(msg,(callstack + 1))
        return self.__logger.warn('%s'%(inmsg))

    def debug(self,msg,callstack=1):
        inmsg = msg
        if callstack is not None:
            inmsg = self.format_call_msg(msg,(callstack + 1))
        return self.__logger.debug('%s'%(inmsg))

    def fatal(self,msg,callstack=1):
        inmsg = msg
        if callstack is not None:
            inmsg = self.format_call_msg(msg,(callstack + 1))
        return self.__logger.fatal('%s'%(inmsg))

class MinNumber(_LoggerObject):
    keywords = ['lineno']
    maxval = 0xffffffffffffffff
    def __init__(self):
        super(MinNumber,self).__init__('disttools')
        self.lineno = self.__class__.maxval
        return

    def __getattr__(self,key,defval):
        if key in self.__dict__.keys():
            return self.__dict__[key]
        return self.__class__.maxval

    def __setattr__(self,key,val):
        if not key.startswith('_'):
            if self.__getattr__(key,self.__class__.maxval) > val:
                self.__dict__[key] = val
            return
        self.__dict__[key] = val
        return

    def __str__(self):
        s = '{'
        i = 0
        for k in dir(self):
            if k.startswith('_'):
                continue
            if i > 0 :
                s += ';'
            s += '%s=%s'%(k,self.__dict__[k])
            i += 1
        s += '}'
        return s

class FilterSource(_LoggerObject):
    def __init__(self):
        super(FilterSource,self).__init__('disttools')
        self.__statics = []
        self.__code = dict()
        self.__names = dict()
        return

    def add_code(self,lineno,source,name):
        self.__code[lineno] = source
        self.__names[lineno] = name
        return

    def add_static(self,source):
        self.__statics.append(source)
        return

    def __str__(self):
        s = ''
        for c in self.__statics:
            s += '%s'%(c)
        s += '\n'
        for l in sorted(self.__code.keys()):
            logging.info('[%d] %s'%(l,self.__names[l]))
            s += '%s'%(self.__code[l])
        return s

def release_runcmd(cmd):
    plog = _LoggerObject('disttools')
    plog.debug('run cmd [%s]'%(cmd))
    #logging.info('runcmd (%s)'%(cmd))
    p = subprocess.Popen(cmd,shell=True)
    if sys.version[0] != '2':
        # we cheat the python3 to not give the warning
        p.returncode = 0
    plog = None
    return p

def get_tempd():
    unamever = platform.uname()[0]
    if unamever.lower() == 'windows':
        return os.environ['TEMP']
    elif unamever.lower() == 'linux' or unamever.lower() == 'darwin' or unamever.lower().startswith('cygwin_'):
        if 'TEMP' in os.environ.keys():
            return os.environ['TEMP']
        elif 'TMP' in os.environ.keys():
            return os.environ['TMP']
        else:
            return '/tmp'
    else:
        raise Exception('not supported os %s'%(platform.uname()[0]))
    return '/tmp'

copyfile_python_command='''
#! /usr/bin/env python

import argparse
import sys
import logging
import time
import subprocess
import re
import os

def make_dir_safe(d=None):
	if d is not None:
		if not os.path.isdir(d):
			try:
				os.makedirs(d)
			except:
				pass
		if not os.path.isdir(d):
			raise Exception(\'can not mkdir [%s]\'%(d))

def copy_file(fromfile,tofile):
	fin = open(fromfile,\'rb\')
	dname = os.path.dirname(tofile)
	if len(dname) == 0:
		dname = \'.\'
	make_dir_safe(dname)
	fout = open(tofile,\'wb\')

	for l in fin:
		fout.write(l)
	fin.close()
	fout.close()
	fin = None
	fout = None
	return

def touch_file(outfile):
	with open(outfile,\'wb\') as fout:
		if sys.version[0] == \'2\':
			fout.write(\'\')
		else:
			fout.write(b\'\')
	return

def trans_to_string(s):
    if sys.version[0] == \'3\':
        encodetype = [\'UTF-8\',\'latin-1\']
        idx=0
        while idx < len(encodetype):
            try:
                return s.decode(encoding=encodetype[idx])
            except:
                idx += 1
        raise Exception(\'not valid bytes (%s)\'%(repr(s)))
    return s


def __find_pid_win32(pid):
	cmds = \'wmic process where(ProcessId=%d) get ProcessId\'%(pid)
	devnullfd = open(os.devnull,\'w\')
	p = subprocess.Popen(cmds,stdin=None,stdout=subprocess.PIPE,stderr=devnullfd,shell=True,env=None)
	res = False
	idx = 0
	intexpr = re.compile(\'^([\\d]+)$\')
	if p.stdout is not None:
		for line in iter(p.stdout.readline, b\'\'):
			idx += 1
			s = trans_to_string(line)
			s = s.rstrip(\'\\r\\n\')
			logging.debug(\'[%d][%s]\'%(idx,s))
			m = intexpr.findall(s)
			if m is None or len(m) == 0:
				continue
			findpid = int(m[0])
			if findpid == pid:
				res = True
		p.stdout.close()
		p.stdout = None

	# now to wait for exit
	while True:
		if p is None:
			break
		pret = p.poll()
		if pret is not None:
			break
		time.sleep(0.1)
	p = None
	devnullfd.close()
	devnullfd = None
	return res

def __find_pid_unix_cmd(pid,cmds):
	logging.info(\'run cmd [%s]\'%(cmds))
	devnullfd = open(os.devnull,\'w\')
	p = subprocess.Popen(cmds,stdin=None,stdout=subprocess.PIPE,stderr=devnullfd,shell=True,env=None)
	res = False
	intexpr = re.compile(\'^\\s+([\\d]+)\\s+.*\')
	idx = 0
	if p.stdout is not None:
		for line in iter(p.stdout.readline, b\'\'):
			idx += 1
			s = trans_to_string(line)
			s = s.rstrip(\'\\r\\n\')
			logging.debug(\'[%d][%s]\'%(idx,s))
			m = intexpr.findall(s)
			if m is None or len(m) == 0:
				continue
			findpid = int(m[0])
			if findpid == pid:
				res = True
		p.stdout.close()
		p.stdout = None
	# now to wait for exit
	while True:
		if p is None:
			break
		pret = p.poll()
		if pret is not None:
			break
		time.sleep(0.1)
	p = None
	devnullfd.close()
	devnullfd = None
	return res



def find_pid(pid):
	plat = sys.platform.lower()
	if plat == \'win32\':
		return __find_pid_win32(pid)
	elif plat == \'cygwin\' :
		return __find_pid_unix_cmd(pid,\'ps -W -e\')
	elif plat == \'linux\' or plat == \'linux2\' or plat == \'darwin\':
		return __find_pid_unix_cmd(pid,\'ps -e\')
	else:
		raise Exception(\'not support platform [%s]\'%(plat))
	return False

def set_log_level(args):
    loglvl= logging.ERROR
    if args.verbose >= 3:
        loglvl = logging.DEBUG
    elif args.verbose >= 2:
        loglvl = logging.INFO
    elif args.verbose >= 1 :
        loglvl = logging.WARN
    # we delete old handlers ,and set new handler
    logging.basicConfig(level=loglvl,format=\'%(asctime)s:%(filename)s:%(funcName)s:%(lineno)d\\t%(message)s\')
    return


def copyfile_handler(args,parser):
	set_log_level(args)
	logging.info(\'args %s\'%(repr(args)))
	if args.pid is not None:
		# wait for this pid to wait the process to exit
		while find_pid(args.pid):
			time.sleep(0.1)
	else:
		# wait for time
		stime = time.time()
		etime = (stime + args.wait)
		ctime = stime
		while (ctime < etime):
			time.sleep((etime - ctime))
			ctime = time.time()
	# now we should copy the file
	copy_file(args.args[0],args.args[1])
	if args.touch is not None:
		touch_file(args.touch)
	sys.exit(0)
	return



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(\'--verbose\',\'-v\',default=0,dest=\'verbose\',help=\'set verbose mode\',action=\'count\')
	parser.add_argument(\'--touch\',\'-T\',default=None,dest=\'touch\',help=\'set touched file after copy\',action=\'store\')
	parser.add_argument(\'--pid\',\'-p\',default=None,dest=\'pid\',help=\'specified to wait for pid to exit\',type=int)
	parser.add_argument(\'--wait\',\'-w\',default=1.0,dest=\'wait\',help=\'specify how long to wait in seconds\',type=float)
	parser.add_argument(\'args\',metavar=\'N\',type=str,nargs=2,help=\'fromfile tofile\')
	args = parser.parse_args()
	copyfile_handler(args,parser)
	return

if __name__ == \'__main__\':
	main()
'''

def __get_tab_line(fmt,tabs=0):
    s = ' ' * tabs * 4
    s += fmt
    s += '\n'
    return s

def release_copy_own(tempf,tofile=None,timewait=None):
    cmd =''
    runcmd = ''
    if tofile is None:
        m = importlib.import_module('__main__')
        tofile = os.path.abspath(m.__file__)
    touchfile = os.path.join(os.path.dirname(tofile),'%s.touched'%(os.path.basename(tofile)))
    tempd='%s'%(get_tempd())
    fd ,pythonfile = tempfile.mkstemp(suffix='.py',prefix=os.path.join(tempd,'copy'),dir=None,text=True)
    os.close(fd)
    cmd += __get_tab_line(r'#! /usr/bin/env python')
    cmd += copyfile_python_command
    pythonfile = os.path.abspath(pythonfile)
    if timewait is None:
        runcmd = '%s %s --pid %d --touch "%s" "%s"  "%s"'%(sys.executable,pythonfile,os.getpid(),touchfile,tempf,tofile)
    else:
        runcmd = '%s %s --wait %s --touch "%s" "%s" "%s"'%(sys.executable,pythonfile,timewait,touchfile,tempf,tofile)
    with open(pythonfile,'w+') as f:
        #logging.info('cmd %s'%(cmd))
        f.write(cmd)
    release_runcmd(runcmd)
    return



class release_excludes(_LoggerObject):
    def __init__(self):
        super(release_excludes,self).__init__('disttools')
        self.__passlines = dict()
        self.__changelines = dict()
        self.__changestr = dict()
        return


    def add_pass_lines(self,name,start,end):
        self.__passlines[name] = [start,end]
        return

    def is_passed(self,lineno):
        for k in self.__passlines.keys():
            if lineno >= self.__passlines[k][0] and lineno < self.__passlines[k][1]:
                return True
        return False

    def add_change_lines(self,name,start,end,chgstr):
        self.__changelines[name] = [start,end]
        self.__changestr[name] = chgstr
        return

    def is_changed(self,lineno):
        for k in self.__changelines.keys():
            if lineno == self.__changelines[k][0]:
                return 2
            elif lineno > self.__changelines[k][0] and lineno < self.__changelines[k][1]:
                return 1
        return 0

    def get_changed(self,lineno):
        for k in self.__changelines.keys():
            if lineno == self.__changelines[k][0]:
                return self.__changestr[k]
            elif lineno > self.__changelines[k][0] and lineno < self.__changelines[k][1]:
                return self.__changestr[k]
        return None


    def __str__(self):
        s = '@'
        if len(self.__passlines.keys()) > 0:
            s += '<passed>:{'
            i = 0
            for k in self.__passlines.keys():
                if i > 0:
                    s += ';'
                s += '%s:[%d,%d]'%(k,self.__passlines[k][0],self.__passlines[k][1])
                i += 1
            s += '}'
        if len(self.__changelines.keys()) > 0:
            s += '<changed>:{'
            i = 0
            for k in self.__changelines.keys():
                if i > 0:
                    s += ';'
                s += '%s:[%d,%d]'%(k,self.__changelines[k][0],self.__changelines[k][1])
                i += 1
            s += '}'
        return s


class release_filter(release_excludes):
    def __init__(self):
        super(release_filter,self).__init__()
        self.__expats = []
        self.__cmdchgpats = []
        self.__macrostart = []
        self.__macroend = []
        self.__replace = dict()
        self.__replacekeys = []
        return
    def add_expats(self,pat=[],ignore=False):
        for p in pat:
            self.add_expat(p,ignore)
        return

    def add_expat(self,pattern,ignore=False):
        if ignore:
            self.__expats.append(re.compile(pattern,re.I))
        else:
            self.__expats.append(re.compile(pattern))
        return

    def add_replacer(self,origpat,destpat):
        self.info('origpat [%s] destpat [%s]'%(origpat,destpat))
        self.__replace[origpat] = destpat
        # we make sure longest match first
        self.__replacekeys = []
        keys = []
        for k in self.__replace.keys():
            keys.append(k)
        i = 0
        while i < len(keys):
            j = (i+1)
            while j < len(keys):
                if len(keys[j]) < len(keys[i]):
                    tmp = keys[j]
                    keys[j] = keys[i]
                    keys[i] = tmp
                j += 1
            i += 1
        self.__replacekeys = keys
        return

    def add_replacers(self,repls=dict()):
        for k in repls.keys():
            self.add_replacer(k,repls[k])
        return

    def add_cmdchg(self,keypattern,ignore=False):
        if ignore:
            self.__cmdchgpats.append(re.compile(keypattern,re.I))
        else:
            self.__cmdchgpats.append(re.compile(keypattern))
        return

    def add_cmdchgs(self,pats=[],ignore=False):
        for p in pats:
            self.add_cmdchg(p,ignore)
        return

    def add_macro(self,startmacro,endmacro,ignore=False):
        if ignore:
            self.__macrostart.append(re.compile(startmacro,re.I))
            self.__macroend.append(re.compile(endmacro,re.I))
        else:
            self.__macrostart.append(re.compile(startmacro))
            self.__macroend.append(re.compile(endmacro))
        return

    def add_macros(self,macros=[],ignore=False):
        for m in macros:
            assert(len(m)==2)
            self.add_macro(m[0],m[1],ignore)
        return

    def __process_excludes(self,m,callback=None,ctx=None):
        for d in dir(m):
            v = getattr(m,d,None)
            self.info('[%s].%s'%(m.__name__,d))
            if callback is not None:
                callback(d,v,ctx)
            excluded = False
            for ex in self.__expats:
                if ex.match(d):
                    excluded = True
                    break
            if excluded:
                if inspect.isclass(v) or inspect.isfunction(v) or \
                    inspect.ismethod(v):
                    s,l=inspect.getsourcelines(v)
                    self.add_pass_lines(d,l,l + len(s))
                else:
                    self.warn('%s not in the call method or function mode'%(d))
                continue
            cmdchg = -1
            i = 0
            for ex in self.__cmdchgpats:
                if ex.match(d):
                    cmdchg = i
                    break
                i += 1
            if cmdchg >= 0:
                if inspect.isfunction(v) :
                    s,l=inspect.getsourcelines(v)
                    decls = s[0]
                    decls = decls.rstrip('\r\n')
                    chgpat = '%s\n'%(decls)
                    chgpat += '    raise Exception(\'%s not valid in releae mode\')'%(d)
                    self.add_change_lines(d,l,l + len(s),chgpat)
                else:
                    logging.error('%s not function type'%(d))
                continue
        return

    def __get_file_content(self,m):
        file = os.path.abspath(m.__file__)
        if file.endswith('.pyc'):
            file = re.sub('.pyc$','.py',file)
        slines = []
        with open(file,'r') as fin:
            for l in fin:
                l = l.rstrip('\r\n')
                slines.append(l)
        return slines


    def __macro_filter(self,m):
        slines = self.__get_file_content(m)
        i = 0
        filtermacro = -1
        startline = -1
        for l in slines:
            i += 1
            if filtermacro < 0:
                fi =0
                for flt in self.__macrostart:
                    if flt.match(l):
                        filtermacro = fi
                        startline = i
                        break
                    fi += 1
            elif filtermacro >= 0:
                flt = self.__macroend[filtermacro]
                if flt.match(l):
                    endline = i
                    filtermacro = -1
                    filtername = 'filter_start%d_end%d'%(startline,endline)
                    self.add_pass_lines(filtername,startline,endline+1)
                    startline = -1
                    endline = -1
        return

    def process_module(self,m,callback=None,ctx=None):
        self.__process_excludes(m,callback,ctx)
        self.__macro_filter(m)

    def output_string(self,m,shebangomit=False):
        s = ''
        slines = self.__get_file_content(m)
        i = 0
        for l in slines:
            i += 1
            if i == 1 and l.startswith('#') and shebangomit:
                # first shebang not output
                continue
            if self.is_passed(i) or (self.is_changed(i) == 1):
                continue
            elif self.is_changed(i) == 2:
                s += '%s\n'%(self.get_changed(i))
            else:
                chgstr = l
                for p in self.__replacekeys:
                    chgstr = re.sub(p,'%s'%(self.__replace[p]),chgstr)
                self.info('(%s) => (%s) %s'%(l,chgstr,self.__replace.keys()))
                s += '%s\n'%(chgstr)
        return s

    def catch_string(self,m,shebangomit=False):
        s = ''
        slines = self.__get_file_content(m)
        i = 0
        for l in slines:
            i += 1
            if i == 1 and l.startswith('#') and shebangomit:
                continue
            if self.is_passed(i):
                chgstr = l
                for p in self.__replacekeys:
                    chgstr = re.sub(p,'%s'%(self.__replace[p]),chgstr)
                s += '%s\n'%(chgstr)
        return s


def release_get_output(mod,excludes=[],macros=[],cmdchanges=[],repls=dict(),checkcall=None,ctx=None,shebangomit=False):
    flt = release_filter()
    flt.add_expats(excludes)
    flt.add_macros(macros)
    flt.add_cmdchgs(cmdchanges)
    flt.add_replacers(repls)
    flt.process_module(mod,checkcall,ctx)
    return flt.output_string(mod,shebangomit)

def release_get_catch(mod,includes=[],macros=[],repls=dict(),checkcall=None,ctx=None,shebangomit=False):
    flt = release_filter()
    flt.add_expats(includes)
    flt.add_macros(macros)
    flt.add_replacers(repls)
    flt.process_module(mod,checkcall,ctx)
    return flt.catch_string(mod,shebangomit)

def release_write_tempfile(s):
    tempd = get_tempd()
    fd ,writetemp = tempfile.mkstemp(suffix='.py',prefix=os.path.join(tempd,'copy'),dir=None,text=True)
    os.close(fd)
    with open(writetemp,'w+') as fout:
        fout.write('%s'%(s))
    return writetemp


def release_file(modname='__main__',tofile=None,excludes=[],macros=[],cmdchanges=[],repls=dict(),checkcall=None,ctx=None,timewait=None):
    if modname is None:
        modname = '__main__'
    m = importlib.import_module(modname)
    #logging.info('repls keys %s'%(repls.keys()))
    s = release_get_output(m,excludes,macros,cmdchanges,repls,checkcall,ctx)
    # now we should get the file
    writetemp = release_write_tempfile(s)
    return release_copy_own(writetemp,tofile,timewait)


