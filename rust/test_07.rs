// DESCRIPTION: const with strings

fn main() 
{
  const UNAME:&str="Mohtashim";
  const UNAME_LEN:usize = UNAME.len();
  
  println!("name {} length {}",UNAME,UNAME_LEN);
}
