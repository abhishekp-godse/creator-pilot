import React from 'react';
import { Users2, ArrowUpRight, Handshake, Target } from 'lucide-react';

export function CollabMatcherView({ collabs }) {
  if (!collabs || collabs.length === 0) return null;

  return (
    <div className="bg-[#141d2f]/90 border border-slate-800 rounded-2xl p-6 mb-8">
      <div className="flex items-center justify-between mb-4">
        <div>
          <div className="flex items-center gap-2">
            <Handshake className="w-5 h-5 text-indigo-400" />
            <h3 className="text-base font-bold text-white">Peer Collaboration Matcher</h3>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Creators with matching niche overlap (15k–45k subscribers) for cross-promotional growth
          </p>
        </div>
        <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 flex items-center gap-1.5">
          <Users2 className="w-3.5 h-3.5" /> High Synergies Found
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {collabs.map((c, idx) => (
          <div
            key={idx}
            className="p-4 rounded-xl bg-slate-800/40 border border-slate-700/60 hover:border-indigo-500/50 transition flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between mb-2">
                <div>
                  <h4 className="font-bold text-sm text-white">{c.channel_name}</h4>
                  <span className="text-xs text-slate-400">{c.handle}</span>
                </div>
                <div className="text-right">
                  <span className="text-xs font-bold text-emerald-400">{c.niche_overlap_pct}% Overlap</span>
                  <div className="text-[11px] text-slate-400">{c.subscriber_count.toLocaleString()} subs</div>
                </div>
              </div>

              <div className="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800 mt-2">
                <span className="text-[10px] text-indigo-300 font-semibold uppercase tracking-wider block mb-1">
                  Synergistic Video Concept
                </span>
                <p className="text-xs text-slate-300 italic">"{c.collab_video_concept}"</p>
              </div>
            </div>

            <div className="mt-3 pt-2.5 border-t border-slate-700/40 flex items-center justify-between text-[11px]">
              <span className="text-emerald-400 font-medium">{c.reach_potential}</span>
              <button className="flex items-center gap-1 text-indigo-400 hover:text-indigo-300 font-medium">
                Draft Pitch <ArrowUpRight className="w-3 h-3" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
