'use client';
import { useState, useMemo } from 'react';
import styles from './FilterableMenu.module.css';
import cigarsData from '../data/cigars.json';

const CATEGORY_ORDER = ['Signature Collection', 'Premium Selection', 'Curated Selection'];
const CATEGORY_DESC: Record<string, string> = {
  'Signature Collection': 'The iconic marques that define Cuban cigar culture.',
  'Premium Selection': 'Refined expressions for the discerning connoisseur.',
  'Curated Selection': 'A carefully chosen range spanning the world\'s finest tobacco regions.',
};

export default function FilterableMenu() {
  const [activeCategory, setActiveCategory] = useState('Signature Collection');
  const [isExpanded, setIsExpanded] = useState(false);

  const filteredCigars = useMemo(
    () => cigarsData.filter(c => c.category === activeCategory),
    [activeCategory]
  );

  return (
    <section id="menu" className={styles.menuSection}>
      <div className={styles.container}>
        <div className={styles.header}>
          <p className={styles.eyebrow}>The Collection</p>
          <h2 className={styles.title}>Our Curated Cellar</h2>
          <p className={styles.subtitle}>
            Each cigar is personally selected. Ask our team for a recommendation.
          </p>

          <button
            className={styles.toggleMenuBtn}
            onClick={() => setIsExpanded(!isExpanded)}
          >
            {isExpanded ? '— Close Collection' : '+ Explore Collection'}
          </button>
        </div>

        {isExpanded && (
          <div className={`${styles.menuContent} animate-fade-in`}>
            {/* Category tabs */}
            <div className={styles.filters}>
              {CATEGORY_ORDER.map(cat => (
                <button
                  key={cat}
                  className={`${styles.filterBtn} ${activeCategory === cat ? styles.active : ''}`}
                  onClick={() => setActiveCategory(cat)}
                >
                  {cat}
                </button>
              ))}
            </div>

            <p className={styles.catDesc}>{CATEGORY_DESC[activeCategory]}</p>

            <div className={styles.grid}>
              {filteredCigars.map((cigar, index) => (
                <div
                  key={cigar.id}
                  className={styles.card}
                  style={{ animationDelay: `${(index % 12) * 0.04}s` }}
                >
                  <div className={styles.imageContainer}>
                    <img
                      src={`/cigars/${cigar.id}.jpg`}
                      alt={cigar.name}
                      className={styles.cigarImage}
                      onError={(e) => {
                        (e.currentTarget as HTMLImageElement).src =
                          `https://placehold.co/600x160/0a0a0a/FFD369?text=${encodeURIComponent(cigar.name)}`;
                      }}
                    />
                  </div>
                  <div className={styles.cardBody}>
                    <h4 className={styles.cigarName}>{cigar.name}</h4>
                    {cigar.strength && (
                      <span className={styles.strength}>{cigar.strength}</span>
                    )}
                    {cigar.notes && (
                      <p className={styles.notes}>{cigar.notes}</p>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </section>
  );
}
