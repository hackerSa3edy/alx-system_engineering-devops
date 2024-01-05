#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+?[a-zA-Z0-9_-]*)\].*\[to:(\+?[a-zA-Z0-9_-]*)\].*\[flags:(\S*)\]/).join(',')
