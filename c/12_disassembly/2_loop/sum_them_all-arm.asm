4	int sum_them_all(int* arr, int arr_len) {
   0x0000000000000774 <+0>:	sub	sp, sp, #0x20
   0x0000000000000778 <+4>:	str	x0, [sp, #8]
   0x000000000000077c <+8>:	str	w1, [sp, #4]

5	    int sum = 0;
   0x0000000000000780 <+12>:	str	wzr, [sp, #28]

6	    for (int i = 0; i < arr_len; ++i) {
   0x0000000000000784 <+16>:	str	wzr, [sp, #24]
   0x0000000000000788 <+20>:	b	0x7b8 <sum_them_all+68>
   0x00000000000007ac <+56>:	ldr	w0, [sp, #24]
   0x00000000000007b0 <+60>:	add	w0, w0, #0x1
   0x00000000000007b4 <+64>:	str	w0, [sp, #24]
   0x00000000000007b8 <+68>:	ldr	w1, [sp, #24]
   0x00000000000007bc <+72>:	ldr	w0, [sp, #4]
   0x00000000000007c0 <+76>:	cmp	w1, w0
   0x00000000000007c4 <+80>:	b.lt	0x78c <sum_them_all+24>  // b.tstop

7	        sum = sum + arr[i];
   0x000000000000078c <+24>:	ldrsw	x0, [sp, #24]
   0x0000000000000790 <+28>:	lsl	x0, x0, #2
   0x0000000000000794 <+32>:	ldr	x1, [sp, #8]
   0x0000000000000798 <+36>:	add	x0, x1, x0
   0x000000000000079c <+40>:	ldr	w0, [x0]
   0x00000000000007a0 <+44>:	ldr	w1, [sp, #28]
   0x00000000000007a4 <+48>:	add	w0, w1, w0
   0x00000000000007a8 <+52>:	str	w0, [sp, #28]

8	    }
9	    return sum;
   0x00000000000007c8 <+84>:	ldr	w0, [sp, #28]

10	}
   0x00000000000007cc <+88>:	add	sp, sp, #0x20
   0x00000000000007d0 <+92>:	ret

