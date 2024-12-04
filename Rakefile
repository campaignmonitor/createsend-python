
desc "Run tests"
task :test do
  system "pip install tox"
  system "tox --skip-missing-interpreters"
end

desc "Build source and wheel distributions"
task :build do
  system "python setup.py sdist"
  system "python setup.py bdist_wheel"
end

desc "Build and release a source distribution"
task :release do
    # Create source and wheel distributions
    system "python setup.py sdist bdist_wheel"

    # Upload using Twine
    system "python -m twine upload dist/*"
end

task :default => :test
