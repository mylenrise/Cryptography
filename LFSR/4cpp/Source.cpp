//#include <iostream>
//#include <fstream>
//#include <sstream>
//
//using namespace std;
//
//unsigned char GeffeGenerator();
//
// int state1 = 0x4DB270;
// int state2 = 0x1F951D70;
// int state3 = 0x6500C12C;
//
//int main()
//{
//
//	ofstream outf("out.txt", ios::binary);
//	
//
//	stringstream formatter;
//	int n = 1250000;
//
//	for (unsigned i = 0; i < n; ++i)
//	{
//		unsigned char value = 0;
//		for (unsigned int j = 0; j < 8; ++j)
//		{
//			value |= (GeffeGenerator() << (7 - j));
//		}
//
//		outf.write((char *)&value, 1);
//	}
//
//	outf.close();
//
//	return 0;
//}
//
//
//unsigned char LFSR1(int state1)
//{
//
//	if (state1 & 0x00000001)
//	{
//		state1 = ((state1 ^ 0x400016) >> 1) | (1 << 23);
//		return 1;
//	}
//	else
//	{
//		state1 >>= 1;
//		return 0;
//	}
//}
//
//unsigned char LFSR2(int state2)
//{
//	if (state2 & 0x00000001)
//	{
//		state2 = ((state2 ^ 0x1000000E) >> 1) | (1 << 29);
//		return 1;
//	}
//	else
//	{
//		state2 >>= 1;
//		return 0;
//	}
//}
//
//unsigned char LFSR3(int state3)
//{
//	
//	if (state3 & 0x00000001)
//	{
//		state3 = ((state3 ^ 0x40000016) >> 1) | (1 << 31);
//		return 1;
//	}
//	else
//	{
//		state3 >>= 1;
//		return 0;
//	}
//}
//unsigned char GeffeGenerator()
//{
//	unsigned char first = LFSR1(state1);
//	unsigned char second = LFSR2(state2);
//	unsigned char third = LFSR3(state3);
//	return (first & second) ^ (second & third) ^ third;
//}