
desc "Run tests"
task :test do
  # Depends on nose being installed: pip install nose
  system "nosetests --with-coverage --cover-erase --cover-package=createsend --cover-html"
end

desc "Build a source distribution"
task :build do
  system "python setup.py sdist"
end

desc "Build and release a source distribution"
task :release do
  system "python setup.py sdist upload"
end

task :default => :test
