fun unless(condition: Boolean, block: () -> Unit) {
    if (!condition) {
        block()
    }
}
​
fun until(condition: () -> Boolean, block: () -> Unit) {
    while (!condition()) {
        block()
    }
}
​
fun forceRun(block: () -> Unit) {
    try {
        block()
    } catch (e: Throwable) { }
}