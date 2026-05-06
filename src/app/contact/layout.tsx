import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Contact & Location | CNX Cigars Chiang Mai',
  description: 'Visit us at NPARC Chiang Mai. View our opening hours, location, and contact details for the best cigar lounge in Northern Thailand.',
};

export default function ContactLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
