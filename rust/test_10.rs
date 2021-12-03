// DESCRIPTION: string new push_str push(char)

fn main()
{
  let mut z = String::new();
  
  z.push_str("hell");
  
  println!("{}",z);
  
  z.push('o');
  
  println!("{}",z);
}
