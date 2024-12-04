
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
***REMOVED******REMOVED***# Create source and wheel distributions
***REMOVED******REMOVED***system "python setup.py sdist bdist_wheel"

***REMOVED******REMOVED***# Upload using Twine
***REMOVED******REMOVED***system "python -m twine upload dist/*"
end

task :default => :test
