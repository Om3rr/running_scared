require 'fileutils'
p "test"
FileUtils.mkdir_p("output")
File.open("output/hazilim", "w"){|f| f.write "Malalalallalalalla milim"}
sleep(2.hours)
p ":("
