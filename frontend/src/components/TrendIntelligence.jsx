import React from 'react';
import { Compass, Flame, Hourglass, Sparkles } from 'lucide-react';

export function TrendIntelligence({ trends, onSelectHook }) {
  if (!trends || trends.length === 0) return null;

  return (
    <div className="bg-[#141d2f]/90 border border-slate-800 rounded-2xl p-6 mb-8">
      <div className="flex items-center justify-between mb-4">
        <div>
          <div className="flex items-center gap-2">
            <Compass className="w-5 h-5 text-indigo-400" />
            <h3 className="text-base font-bold text-white">Niche Trend Intelligence Engine</h3>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Real-time keyword momentum, semantic niche-fit matching, and trend decay timers
          </p>
        </div>
        <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 flex items-center gap-1.5">
          <Flame className="w-3.5 h-3.5 text-amber-400" />
          Live Google Trends
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {trends.map((t, idx) => (
          <div
            key={idx}
            className="p-4 rounded-xl bg-slate-800/40 border border-slate-700/60 hover:border-indigo-500/50 transition flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between gap-1 mb-2">
                <span className="text-[10px] font-semibold uppercase tracking-wider text-slate-400">
                  {t.category}
                </span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                  {t.fit_score}% Fit
                </span>
              </div>

              <h4 className="font-bold text-sm text-white leading-snug">{t.topic}</h4>

              <div className="flex items-center gap-2 my-2.5 text-xs">
                <span className="text-emerald-400 font-semibold">{t.search_volume_velocity}</span>
                <span className="text-slate-500">•</span>
                <span className="flex items-center gap-1 text-slate-400">
                  <Hourglass className="w-3 h-3 text-amber-400" />
                  Expires in {t.expires_in_days}d
                </span>
              </div>

              <div className="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800 mt-2">
                <div className="flex items-center gap-1 text-[10px] text-indigo-300 font-semibold uppercase tracking-wider mb-1">
                  <Sparkles className="w-3 h-3 text-indigo-400" />
                  Recommended Hook
                </div>
                <p className="text-xs text-slate-300 italic">"{t.recommended_hook}"</p>
              </div>
            </div>

            <button
              onClick={() => onSelectHook && onSelectHook(t.recommended_hook)}
              className="w-full mt-3 py-1.5 rounded-lg bg-slate-700/50 hover:bg-slate-700 text-xs font-semibold text-slate-200 transition text-center"
            >
              Test Title in Scorer
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
