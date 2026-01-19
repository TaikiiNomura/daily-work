use proconio::input;
fn main() {
  input! {
    p: i32,
    q: i32,
    x: i32,
    y: i32,
  }
  if p<=x && x<=p+99 && q<=y && y<=q+99{
    println!("Yes");
  } else {
    println!("No");
  }
}
