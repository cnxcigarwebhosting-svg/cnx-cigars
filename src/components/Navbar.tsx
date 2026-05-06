'use client';
import Link from 'next/link';
import Image from 'next/image';
import { useState, useEffect } from 'react';
import styles from './Navbar.module.css';

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  return (
    <header className={`${styles.navbar} ${scrolled ? styles.scrolled : ''}`}>
      <nav className={styles.container}>
        <div className={styles.logo}>
          <Link href="/" style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <Image src="/logo.png" alt="CNX Cigars Logo" width={38} height={38} className={styles.logoImage} />
            <span>CNX <span className={styles.gold}>CIGARS</span></span>
          </Link>
        </div>
        <div className={styles.links}>
          <Link href="/#experience">Experience</Link>
          <Link href="/#story">Our Story</Link>
          <Link href="/#menu">Collection</Link>
          <Link href="/reservation" className={styles.ctaLink}>Reserve a Seat</Link>
          <Link href="/contact">Contact</Link>
        </div>
      </nav>
    </header>
  );
}
