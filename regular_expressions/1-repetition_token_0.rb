#!/usr/bin/env ruby
# This script matches the exact word "School" in the input string

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

input = ARGV[0]
matches = input.scan(/School/)

puts matches.join
