use proconio::input;
fn main() {
  // println!("{}", 'A' as i32); // 65
  // println!("{}", 'Z' as i32); // 90
  input! {
    s: String,
  }
  let mut ans = String::new();
  for c in s.chars() {
    // println!("{}", c);
    if 65 <= c as i32 && c as i32 <= 90 {
      ans.push(c);
    }
  }
  println!("{}", ans);
}
