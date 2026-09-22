public class Kata {
    public static String describeShape(Object obj) {
        return switch (obj) {
            case null -> "null";
            case Point(int x, int y) -> "Point(" + x + "," + y + ")";
            case Rectangle(int w, int h) -> "Rectangle " + w + "x" + h;
            case Circle(int r) -> "Circle r=" + r;
            case CenteredCircle(Point(int x, int y), int r) -> "CenteredCircle((" + x + "," + y + "), r=" + r + ")";
            default -> "unknown";
        };
    }
}