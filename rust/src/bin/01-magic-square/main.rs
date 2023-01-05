#[derive(Debug)]
struct MagicSquare(Vec<Vec<usize>>);

impl MagicSquare {
    fn new(n: usize) -> Self {
        assert_eq!(n % 2, 1);

        Self(vec![vec![0; n]; n])
    }

    fn print(&self) {
        for row in &self.0 {
            for value in row {
                print!("{} ", value);
            }
            println!();
        }
    }
}

pub fn main() {
    let magic_square = MagicSquare::new(3);
    magic_square.print();
}
