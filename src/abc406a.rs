use proconio::input;
fn main() {
  input! {
    a: u32,
    b: u32,
    c: u32,
    d: u32,
  }
  if (a*60 + b)>(c*60 + d) {
    println!("Yes");
  } else {
    println!("No");
  }
}
