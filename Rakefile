
desc "Run tests"
task :test do
***REMOVED***system "pip install tox"
***REMOVED***system "tox --skip-missing-interpreters"
end

desc "Build source and wheel distributions"
task :build do
***REMOVED***system "python setup.py sdist"
***REMOVED***system "python setup.py bdist_wheel"
end

desc "Build and release a source distribution"
task :release do
***REMOVED***system "python setup.py sdist upload"
***REMOVED***system "python setup.py bdist_wheel upload"
end

task :default => :test
