double srednia(long *tab, int roz){
	int i;
	double s =0;
	for(i=0;i<roz;i++){
		s+=tab[i];
	}
	return s/roz;
}

double mediana(long *tab, int roz){
	double m;
	if(roz%2) m=tab[roz/2];
	else m=(tab[roz/2-1]+tab[roz/2])/2;
	return m;
}


double moca(int n, double a, double b){
	double x, y;
	int i,li;
	li=0;
	srand(time(NULL));
	for(i=0; i<n; i++){
		x=((double)rand()/(RAND_MAX))+a;
		y=(double)rand()/(RAND_MAX);
		double f = (3-sin(x*x))/(1+x);
		if(f>y) li++;
	}
	double prawd = (double)li/n;
	return prawd;
}


