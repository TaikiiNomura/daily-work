use proconio::input;
fn main(){
  input!{
    mut x:usize,
    mut y:usize,
    z:usize,
  }
  for _ in 0..100_001{
    if x==y*z{
      println!("Yes");
      return;
    }
    x+=1;
    y+=1;
  }
  println!("No");
}
