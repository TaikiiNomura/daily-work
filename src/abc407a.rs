use proconio::input;
fn main() {
  input! {
    a: f32,
    b: f32,
  }
  let mut c: f32 = a / b;
  let mut d: f32 = c - c.floor();
  if d > 0.5 {
    println!("{}", c.floor() as i32 + 1);
  } else {
    println!("{}", c.floor());
  }
}