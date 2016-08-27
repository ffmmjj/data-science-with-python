If you have faced the error "ValueError: unknown locale: UTF-8" on MacOS X, here's the quick fix - add these lines to your ~/.bash_profile:

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8