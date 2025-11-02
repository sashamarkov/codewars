def wait_on_threads(threads)
  threads.each(&:join)
end