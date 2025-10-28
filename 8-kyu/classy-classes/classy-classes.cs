public class Person {
    private readonly string _name;
​
    private readonly int _age;
​
    public Person( string name, int age ) {
        _name = name;
        _age = age;
    }
​
    public string Info {
        get { return string.Format( "{0}s age is {1}", _name, _age ); }
    }
}