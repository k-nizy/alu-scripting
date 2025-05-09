#!/usr/bin/env ruby
# This script matches strings that start with 'hb', followed by 2 or more 't's, and end with 'n'

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

input = ARGV[0]
if input.match?(/^hbt{2,}n$/)
  puts "Correct output with #{input}"
else
  puts ""
end
