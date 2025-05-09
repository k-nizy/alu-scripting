#!/usr/bin/env ruby
# Matching patterns starting with 'h', ending with 'n', with any single character in between

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

input = ARGV[0]
matches = input.scan(/h.n/)

puts matches.join
