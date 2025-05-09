#!/usr/bin/env ruby
# This script matches only capital letters (A-Z)

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

input = ARGV[0]
matches = input.scan(/\p{Upper}/)

puts matches.join
