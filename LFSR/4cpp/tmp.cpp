#include <iostream>
#include <fstream>


static int state1 = 0x4DB270;
static int state2 = 0x1F951D70;
static int state3 = 0x6500C12C;


char LFSR(int &state, int polynom) {

	if (state & 0x00000001)
	{
		state = ((state ^ polynom) >> 1) | (1 << 23);
		return 1;
	}
	else
	{
		state >>= 1;
		return 0;
	}

}
unsigned char generator()
{
	int polynom1 = 0x4DB270;
	int polynom2 = 0x1F951D70;
	int polynom3 = 0x6500C12C;
	char l1 = LFSR(state1, polynom1);
	char l2 = LFSR(state2, polynom2);
	char l3 = LFSR(state3, polynom3);
	return (l1 & l2) ^ (l2 & l3) ^ l3;
}

int main()
{

	std::ofstream fout("out.dat", std::ios::binary);


	
	int n = 1250000;

	for (int i = 0; i < n; ++i)
	{
		char value = 0;
		for (unsigned int j = 0; j < 8; ++j)
		{
			value |= (generator() << (7 - j));
		}

		fout.write((char *)&value, 1);
	}

	fout.close();

	return 0;
}
