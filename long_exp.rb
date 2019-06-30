100.times do |j|
  t = [0.1,0.5,1,1.3,1.5,1.8].sample
  5.times do |i|
    p "Hello im in #{j}:#{i} iter"
    sleep(t)
  end
end
