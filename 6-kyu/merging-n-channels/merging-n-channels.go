package kata
​
func Merge(c ...chan string) <-chan string {
    out := make(chan string)
    if len(c) == 0 {
        close(out)
        return out
    }
    done := make(chan struct{})
    for _, ch := range c {
        go func(ch chan string) {
            for v := range ch {
                out <- v
            }
            done <- struct{}{}
        }(ch)
    }
    go func() {
        for range c {
            <-done
        }
        close(out)
    }()
    return out
}