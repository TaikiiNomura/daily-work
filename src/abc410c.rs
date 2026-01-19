use proconio::input;
fn main(){
  input!{
    n: usize,
    q: usize,
  }
  let mut a: Vec<i32> = (1..=n as i32).collect();
  let mut head: usize = 0; // 先頭のインデックス
  for _ in 0..q{
    input!{t: usize,}
    match t{
      1 => {
        input!{p: usize,x: i32,}
        let idx: usize = (head + p-1) % n; // 先頭からp-1番目の数字を探す
        a[idx]=x;
      }
      2 => {
        input!{p: usize,}
        let idx: usize = (head + p-1) % n;
        println!("{}",a[idx]);
      }
      3 => {
        input!{k: usize,}
        head = (head + k) % n; // ずらす
      }
      _ => unreachable!(),
    }
  }
}
