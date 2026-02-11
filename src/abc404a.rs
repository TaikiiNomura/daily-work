use proconio::input;

fn solve(s: String) {
  let v: Vec<char> = s.chars().collect();
  for c in 'a'..='z' {
    if !v.contains(&c) {
      println!("{}", c);
      return;
    }
  }
}

fn main() {
  input! {
    s: String,
  }
  solve(s);
}
