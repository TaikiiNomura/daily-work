use proconio::input;
fn main(){
  input!{
    mut x:usize,
    y:usize,
  }
  for _i in 0..y{
    x*=2;
  }
  println!("{}",x);
}
