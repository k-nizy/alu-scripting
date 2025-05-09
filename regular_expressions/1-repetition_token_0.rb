#!/usr/bin/env ruby
# Matches strings starting with 'hb', followed by any number of 't's, ending with 'n'

input = ARGV[0] || ""
matches = input.match(/^hbt{2,3}n$|^hbt{6}n$/)

puts matches ? matches[0] : ""
