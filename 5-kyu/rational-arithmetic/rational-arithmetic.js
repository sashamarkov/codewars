        const g = gcd(this.numerator, this.denominator);
        this.numerator /= g;
        this.denominator /= g;
    }
​
    equals(b) {
        return this.numerator === b.numerator && this.denominator === b.denominator;
    }
​
    lessThan(b) {
        return this.numerator * b.denominator < b.numerator * this.denominator;
    }
​
    greaterThan(b) {
        return this.numerator * b.denominator > b.numerator * this.denominator;
    }
​
    lessThanOrEquals(b) {
        return this.numerator * b.denominator <= b.numerator * this.denominator;
    }
​
    greaterThanOrEquals(b) {
        return this.numerator * b.denominator >= b.numerator * this.denominator;
    }
​
    add(b) {
        return new Rational(
            this.numerator * b.denominator + b.numerator * this.denominator,
            this.denominator * b.denominator
        );
    }
​
    sub(b) {
        return new Rational(
            this.numerator * b.denominator - b.numerator * this.denominator,
            this.denominator * b.denominator
        );
    }
​
    mul(b) {
        return new Rational(
            this.numerator * b.numerator,
            this.denominator * b.denominator
        );
    }
​
    div(b) {
        return new Rational(
            this.numerator * b.denominator,
            this.denominator * b.numerator
        );
    }
}