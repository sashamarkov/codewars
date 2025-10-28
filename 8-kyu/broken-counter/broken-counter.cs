public class Counter {
    private int _value;
​
    public int Value {
        get { return _value; }
        set { _value = value; }
    }
​
    public Counter( ) {
        Value = 0;
    }
​
    public void Increase( ) {
        Value += 1;
    }
​
    public void Reset( ) {
        Value = 0;
    }
}