#![feature(asm)]

#[cfg(any(target_arch = "x86", target_arch = "x86_64"))]

fn main() 
{
  let x: u64;
  
  unsafe 
  {
    asm!("mov {}, 5", out(reg) x);
  }

  assert_eq!(x, 5);
  
  println!("value of x = {}",x);
}


