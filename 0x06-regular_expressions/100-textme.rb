#!/usr/bin/env ruby
#This script puts output: [SENDER], [RECEIVER], [FLAGS]
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
