fn main()
{
    unsafe 
    {
        asm! 
        {"
            push %fs                
            pip  %fs
        "};
    }
}


