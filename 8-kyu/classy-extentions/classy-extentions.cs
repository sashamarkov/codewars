public class Cat : Animal {
​
    private readonly string _name;
​
    public Cat( string name )
        : base( name ) {
        _name = name;
    }
​
    public override string Speak( ) {
        return string.Format( "{0} meows.", _name );
    }
​
}