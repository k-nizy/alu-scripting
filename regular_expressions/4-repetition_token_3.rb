#!/usr/bin/env ruby
# Matching patterns starting with 'h', followed by exactly 2 'b's, then 't' and ending with 'n'

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

input = ARGV[0]
matches = input.scan(/hb{2}tn/)

puts matches.join
