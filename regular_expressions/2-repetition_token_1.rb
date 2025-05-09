#!/usr/bin/env ruby
# This script matches variations of 'School' with optional extra 'o's

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

input = ARGV[0]
matches = input.scan(/Scho+l/)

puts matches.join
