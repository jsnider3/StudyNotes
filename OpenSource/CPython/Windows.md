# CPython - Windows Specific Notes

## Windows

* Install msbuild (Visual Studio takes a while to install.) and
  add it to your path. Make sure to install Visual C++ with Visual
  Studio, failure to do so can cause `cannot find vcvarsall.bat` errors.
* Install TortoiseSVN with the command line options and add svn.exe
  to your path.
* Run `PCBuild/build.bat -e`. Remove the `-e` after the first time.
* Python -m test -j3
* UAC may ask you for permission to run some of the networking tests.

## Windows Deprecation Warnings

I saw a number of networking related deprecation warnings while compiling
python on Windows. I'll mention it to the core team when given an opportunity
and see if I can get approval to fix them.

Screenshots of these warnings are provided as DeprecationScreenshot.png
and MoreDeprecation.png

## Windows Test Failure

I noticed test_subprocess fail on my machine on
lib/test/test_subprocess.py:2553.

Is this a failure of the test or a failure of the code? I suspect the
first.

Test doesn't fail on Windows.

Turns out this was already reported as issue 26782. As expected, it was
a bad test.

## test_threaded_import

This one took 2,039 seconds to complete. Is that supposed to happen?
