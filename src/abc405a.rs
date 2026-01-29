use proconio::input;
fn main() {
  input! {
    r: i32,
    x: i32,
  }
  if x == 1 && 1600 <= r && r < 3000 {
    println!("Yes");
  } else if x == 2 && 1200 <= r && r < 2400 {
    println!("Yes");
  } else {
    println!("No");
  }
}
