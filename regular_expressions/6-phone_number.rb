#!/usr/bin/env ruby
# This script matches exactly 10-digit phone numbers

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

input = ARGV[0]
matches = input.scan(/\b\d{10}\b/)

puts matches.join
