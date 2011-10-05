
desc "Run tests"
task :test do
***REMOVED***# Depends on nose being installed: pip install nose
***REMOVED***system "nosetests"
end

desc "Build a source distribution"
task :build do
***REMOVED***system "python setup.py sdist"
end

desc "Build and release a source distribution"
task :release do
***REMOVED***system "python setup.py sdist upload"
end

task :default => :test
