use proconio::input;
fn main() {
  input! {
    n: usize,
    mut s: f32,
    t: [f32; n],
  }
  s += 0.5;
  let mut last_time: f32 = 0.0;
  let mut isyes = true;
  for i in 0..n {
    if (t[i] - last_time) >= s {
      isyes = false;
      break;
    }
    last_time = t[i];
  }
  if isyes {
    println!("Yes");
  } else {
    println!("No");
  }
}