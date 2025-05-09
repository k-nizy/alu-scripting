#!/usr/bin/env ruby
# This script matches strings that start with h, end with n, with exactly one character in between

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

input = ARGV[0]
matches = input.scan(/\bh.n\b/)

puts matches.join
