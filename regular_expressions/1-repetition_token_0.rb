#!/usr/bin/env ruby
# This script matches strings starting with 'hb', followed by 2-3 't's, and ending with 'n'

input = ARGV[0] || ""
matches = input.match(/^hbt{2,3}n$/)

puts matches ? matches[0] : ""
