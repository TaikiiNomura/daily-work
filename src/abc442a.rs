use proconio::input;
fn main() {
  input! {
    s: String,
  }
  let mut ans = 0;
  for c in s.chars() {
    if c == 'i' || c == 'j' {
      ans += 1;
    }
  }
  println!("{}", ans);
}
