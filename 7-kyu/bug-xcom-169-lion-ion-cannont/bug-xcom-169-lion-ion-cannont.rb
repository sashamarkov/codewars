def release_ions count
  (1..count).each do |ion_no|
    yield ion_no
  end
end